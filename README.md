You need to authenticate yourself with google for using google documentAI.you can do this by creating new projects in google cloud console and generate access token save path of that json and set it as enviroment variable.

After creating your processor you need to update values of "location","processor_id", and "project_id" with your crendentials.

generate access token from hugging and update in inference.py

Authenticate yourself with firebase by genreting json after cretaing new project and add path of that json as enviroment variable and change storage bucket if you have change from default.

for testing you can visit : "https://ocr-ner.onrender.com/docs"

you need to enter username ,project name that can be anything of your choice and upload your file for OCR and NER.

Note: one user can have multiple projects each containing different file.

