from repository.DocsRepository import DocsRepository

textRepository = DocsRepository()

text = [
    ["Почему именно С#?", "Друзья, я думаю, что многие из вас при просмотре программы курса задались вопросом: почему именно C# был выбран в качестве основного инструмента? Командой GeekBrains было рассмотрено несколько наиболее популярных языков программирования, представленных на экране.На текущем уровне изучения программирования все задачи курса будут решаться одинаково на любом из представленных языков. Отличия будут совершенно незначительны. Написав программу на одном из них, вы всегда сможете переписать ее на другой, изменив только синтаксис. Давайте рассмотрим критерии, по которым язык C# был выбран для текущего курса. "],
    ["Подготовка окружения", "Друзья, отмечу, что наиболее приоритетный вариант настройки окружения – это самостоятельная установка и настройка инструментов разработчика. Однако, если у вас возникнут существенные трудности при настройке окружения, то есть альтернативный вариант. Он заключается в использовании облачного сервиса, который предоставит вам удаленный рабочий стол с установленным Git, .NET и Visual Studio Code. Подключиться и работать с этим сервисом можно напрямую из браузера.Этим сервисом можно воспользоваться в случае, если ваше аппаратное обеспечение не позволяет установить необходимые инструменты. Инструкции по работе с этим сервисом будут также прикреплены к описанию лекции.[Скрин-каст]Сейчас мы рассмотрим процесс настройки окружения. Проделывать это одновременно со мной не нужно, рекомендую внимательно посмотреть, а после лекции можно будет проделать эти шаги самостоятельно.Для установки платформы .NET нам потребуется проделать следующие шаги:перейдем на сайт загрузки установщика платформы .NET (https://dotnet.microsoft.com/en-us/download/dotnet/7.0)загрузим и запустим установщик для вашей платформы. В большинстве случаев это будет 64-разрядный установщик, вам нужно будет выбрать только архитектуру.редактор Visual Studio Code могут быть установлены расширения для удобства разработки. Эти расширения добавляют в редактор подсветку синтаксиса, подсказки разработчику и другие полезные возможности. Откроем Visual Studio Code и для установки расширения откроем соответствующую панель, введем в поиске «C#» и выберем расширение C# for Visual Studio Code (оно будет первым в списке). Для его установки нажмем кнопку Install.На данном этапы мы готовы к написанию программ на C#. В качестве первой программы предлагаю реализовать вывод сообщения «Hello, World!» на экран. О такой программе вы наверняка уже слышали, а может быть, даже её писали. В большинстве случаев, она используется для того, чтобы понять, правильно ли настроено ваше окружение."]
]
terms = [
    ["думаю", "область памяти, предназначения для хранения некоторого значения."],
    ["возникнут", "способом определения типа данных языком программирования."]
]
textRepository.createLectureDocs(terms=terms, text=text)