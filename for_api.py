# pip install -U transformers
# pip install -U accelerate
# pip install tensorflow[and-cuda]
# pip install tensorrt
# pip install datasets
import whisperx # pip install git+https://github.com/m-bain/whisperx.git
import gc
import os

import pandas as pd # pip install pandas
import numpy as np # pip install numpy

import torch # pip install torch
import transformers # pip install transformers
import torch.nn as nn
from transformers import AutoModel, BertTokenizer, BertForSequenceClassification, pipeline, BertForMaskedLM
from transformers import TrainingArguments, Trainer
# from sklearn.metrics import classification_report, f1_scor # pip install -U scikit-learn

import spacy # pip install -U spacy
import copy
import pickle
import random

import spacy
from spacy.lang.ru.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

import wikipedia

nlp = spacy.load("ru_core_news_sm") # python -m spacy download ru_core_news_sm
# Фильтрация предложения по точкам
def filter_dot(result_old=False):
    if (type(result_old) == bool):
        print("result is not defind")

    result = copy.deepcopy(result_old['segments'])
    new_result = []


    for sentence in result:
        if len(new_result) == 0:
            new_result.append(sentence)
        else:
            if (new_result[-1]['text'][-1]) not in '.!?':
                new_result[-1]['end'] = sentence['end']
                new_result[-1]['text'] = new_result[-1]['text'] + sentence['text']
                new_result[-1]['words'] = new_result[-1]['words'] + sentence['words']
            else:
                new_result.append(sentence)

    result_old['segments'] = new_result
    return result_old

# Массив из предложений текста
def all_text_and_sentence_and_word(result=False):
    if (type(result) == bool):
        print("result is not defind")

    result = filter_dot(result)

    data_text = list()

    for sentence in result['segments']:
        data_text.append(sentence['text'])

    result['all_text'] = data_text

    return result


# Загрузка модели
def upload_model_whisperx(model="large"):
    device = "cuda"
    compute_type = "float16"
    model = whisperx.load_model(model, device, compute_type=compute_type, language="ru")
    return model

# Фильирация выявления предложения из текста
def stt(audio_file, model):
    if not(os.path.exists(audio_file)):
        print("file not exist")
        return False

    batch_size = 16
    device = "cuda"

    audio = whisperx.load_audio(audio_file)
    result = model.transcribe(audio, batch_size=batch_size)
    # result = model.transcribe(audio)

    model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
    result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)

    gc.collect()
    torch.cuda.empty_cache()
    del model_a

    result = all_text_and_sentence_and_word(result)

    return result
def get_prediction(trainer,test_dataset):
    test_pred = trainer.predict(test_dataset)
    labels = np.argmax(test_pred.predictions, axis = -1)
    return labels

class Data(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {k: torch.tensor(v[idx]) for k, v in self.encodings.items()}
        item["labels"] = torch.tensor([self.labels[idx]])
        return item
    def __len__(self):
        return len(self.labels)

def get_ans_from_model(list_of_test_texts):
    model_path = "/content/drive/MyDrive/hack/bert-del"
    model = BertForSequenceClassification.from_pretrained(model_path, num_labels=3)
    tokenizer = BertTokenizer.from_pretrained(model_path)
    training_args = TrainingArguments(output_dir = './results', #Выходной каталог
                                    num_train_epochs = 10, #Кол-во эпох для обучения
                                    per_device_train_batch_size = 8, #Размер пакета для каждого устройства во время обучения
                                    per_device_eval_batch_size = 8, #Размер пакета для каждого устройства во время валидации
                                    weight_decay =0.01, #Понижение весов
                                    load_best_model_at_end = True, #Загружать ли лучшую модель после обучения
                                    learning_rate = 1e-5, #Скорость обучения
                                    evaluation_strategy ='epoch', #Валидация после каждой эпохи (можно сделать после конкретного кол-ва шагов)
                                    logging_strategy = 'epoch', #Логирование после каждой эпохи
                                    save_strategy = 'epoch', #Сохранение после каждой эпохи
                                    save_total_limit = 1,
                                    seed=21)

    tester = Trainer(model=model,
                    tokenizer = tokenizer,
                    args = training_args)
    max_seq_len=100

    tokens_test = tokenizer.batch_encode_plus(
        list_of_test_texts,
        max_length = max_seq_len,
        padding = 'max_length',
        truncation = True
    )

    test_dataset = Data(tokens_test, [1]*len(list_of_test_texts))
    return get_prediction(tester, test_dataset)

def get_parts_of_text(list_of_sentences):
    sentences_out = []
    classes_out = []
    for k in range(len(list_of_sentences)):
        text = list_of_sentences[k]

        doc = nlp(text)
        for sentence in doc.sents:
            sentences_out.append(sentence.text)

    classes_out=get_ans_from_model(sentences_out)
    classes_out[0]=0
    classes_out[-1]=2
    final_classes = [0]*len(classes_out)
    ind=0
    knn = 5
    for i in range(len(classes_out)-knn,len(classes_out)):
        final_classes[i]=2
    for i in range(knn,len(classes_out)-knn):
      s=0
      for q in range(knn):
        s+=classes_out[i+q+1]
      for q in range(knn):
        s+=classes_out[i-(q+1)]
      final_classes[i] = s/(knn*2)

    parts = ['','','']
    for i in range(len(final_classes)):
        parts[round(final_classes[i])]+=sentences_out[i]+' '

    return parts,classes_out,final_classes

def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    s=0
    for i in range(len(preds)):
        if(labels[i]==1 and preds[i]==1):
            s+=10
        elif(labels[i]==0 and preds[i]==0):
            s+=5
        elif(labels[i]==0 and preds[i]==1):
            s+=1
        else: s+=0
    return {'Our metrics': (s/10)/len(preds)}

def get_ans_from_opr_model(list_of_test_texts):
    model_path = "/content/drive/MyDrive/hack/bert-opr"
    model = BertForSequenceClassification.from_pretrained(model_path, num_labels=2)
    tokenizer = BertTokenizer.from_pretrained(model_path)
    training_args = TrainingArguments(output_dir = './results', #Выходной каталог
                                    num_train_epochs = 1, #Кол-во эпох для обучения
                                    per_device_train_batch_size = 20, #Размер пакета для каждого устройства во время обучения
                                    per_device_eval_batch_size = 20, #Размер пакета для каждого устройства во время валидации
                                    weight_decay =0.01, #Понижение весов
                                    logging_dir = './logs', #Каталог для хранения журналов
                                    load_best_model_at_end = True, #Загружать ли лучшую модель после обучения
                                    learning_rate = 1e-5, #Скорость обучения
                                    evaluation_strategy ='epoch', #Валидация после каждой эпохи (можно сделать после конкретного кол-ва шагов)
                                    logging_strategy = 'epoch', #Логирование после каждой эпохи
                                    save_strategy = 'epoch', #Сохранение после каждой эпохи
                                    save_total_limit = 1,
                                    seed=21)

    tester = Trainer(model=model,
                    tokenizer = tokenizer,
                    args = training_args)

    max_seq_len=100
    tokens_test = tokenizer.batch_encode_plus(
        list_of_test_texts,
        max_length = max_seq_len,
        padding = 'max_length',
        truncation = True
    )

    test_dataset = Data(tokens_test, [1]*len(list_of_test_texts))

    return get_prediction(tester, test_dataset)

def get_oprs_from_list(list_of_sentances):
  pred = get_ans_from_opr_model(list_of_sentances)
  out=[]
  for i in range(len(pred)):
    if pred[i]: out.append(list_of_sentances[i])
  return out

def get_key_words(list_of_sentences_input):
  model = BertForMaskedLM.from_pretrained('ai-forever/ruBert-large')
  tokenizer = BertTokenizer.from_pretrained('ai-forever/ruBert-large', do_lower_case=False)
  unmasker = pipeline('fill-mask', model=model,tokenizer=tokenizer)
  out=[]

  list_of_sentences = get_oprs_from_list(list_of_sentences_input)

  for i in range(len(list_of_sentences)):
    got = [i for i in unmasker("[MASK] - это термин "+f"{list_of_sentences[i][:-1]}".lower())][0]
    if(got['score']>0.5):
      out.append(got['token_str'])
  return out

def summarize(text, per):
    nlp = spacy.load('en_core_web_sm')
    doc= nlp(text)
    tokens=[token.text for token in doc]
    word_frequencies={}
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    max_frequency=max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency
    sentence_tokens= [sent for sent in doc.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent]+=word_frequencies[word.text.lower()]
    select_length=int(len(sentence_tokens)*per)
    summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
    final_summary=[word.text for word in summary]
    summary=''.join(final_summary)
    return summary

def get_definition(string):
  wikipedia.set_lang("ru")
  try:
    try:
        p = wikipedia.summary(string)
    except wikipedia.DisambiguationError as e:
        list_of_refers =e.options
        s=random.choice(list_of_refers)
        list_of_test=[]
        for i in range(len(list_of_refers)):
          if(list_of_refers[i]!=s):
            list_of_test.append(list_of_refers[i])
        list_of_refers = list_of_test.copy()
        try:
          p = wikipedia.summary(wikipedia.search(s)[0])
        except wikipedia.DisambiguationError as e:
          s=random.choice(list_of_refers)
          list_of_test=[]
          for i in range(len(list_of_refers)):
            if(list_of_refers[i]!=s):
              list_of_test.append(list_of_refers[i])
          list_of_refers = list_of_test.copy()
          try:
            p = wikipedia.summary(wikipedia.search(s)[0])
          except wikipedia.DisambiguationError as e:
            s=random.choice(list_of_refers)
            try:
              p = wikipedia.summary(wikipedia.search(s)[0])
            except:
              p = string+' - определение не найдено'
    except:
        p = string+' - определение не найдено'
    return p

def audio_to_text(path):
    audiomodel = upload_model_whisperx()
    res = stt(path, audiomodel)
    
    parts, tet, qwq = get_parts_of_text(res['all_text'])
    text = ''
    for i in res['all_text']:
        text+=i
    short_descr = summarize(text, 0.01)

    terms = list()
    oprs = get_oprs_from_list(res['all_text'])
    out_2 = get_key_words(oprs)

    for term in out_2:
      terms.append([term, get_definition(term)])

    return {'text': ['Введение': parts[0], 'Основная часть': parts[1], 'Заключение': parts[2]],
            'short_descr': short_descr,
            'terms': terms}