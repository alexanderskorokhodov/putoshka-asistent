import React from "react";
import FileIcon from "../components/FileIcon";

export default function FileUI(
  {fileRef,
  file,
  fileName,
  fileType,
  setFileName,
  setFile,
  setFileType,
  setFileOrig}
) {
  const onFileChange = (event) => {
    if (event.target.files && event.target.files[0]) {
      let reader = new FileReader();
      let f = event.target.files[0];
      setFileName(f.name);
      setFileType(f.type.split("/")[0]);
      if (f.type.split("/")[0] !== "image") {
        let ext = f.name.split(".").pop() + " file";
        setFileType(ext);
      }
      // reader.onload = function(e) {
      //   setFileOrig(e.target.result);
      // };
      setFileOrig(f);
      reader.readAsDataURL(event.target.files[0]);
      setFile(URL.createObjectURL(f));
    }
  };

  let fileUI = (
    <div className="uploadbutton" onClick={() => fileRef.current.click()}>
      <FileIcon />
      <div style={{width:"100%", marginTop: "0.5em", textAlign: "center"}}>Загрузите обложку </div>
      <input
        accept='image/*'
        ref={fileRef}
        onChange={onFileChange}
        multiple={false}
        type="file"
        hidden
      />
    </div>
  );
  if (file) {
    let alt = "";
    if (fileType !== "image") {
      console.log();
      alt = (
        <div className="altimg" onClick={() => fileRef.current.click()}>
          <h3 className="alt">{fileType}</h3>
          <p className="filename">{fileName}</p>
        </div>
      );
    }
    fileUI = (
      <div className="uploaded">
        {alt === "" ? (
          <img src={file} alt="error" onClick={() => fileRef.current.click()} />
        ) : (
          alt
        )}
        <div className="changebutton">
          <input
            accept='image/*'
            ref={fileRef}
            onChange={onFileChange}
            multiple={false}
            type="file"
            hidden
          />
          <p className="uploadeddesc">Нажмите на изображение для изменения</p>
        </div>
      </div>
    );
  }
  return fileUI;
}
