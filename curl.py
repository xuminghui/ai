#langchain的基于抽象语法树的python拆分器
from langchain.text_splitter import RecursiveCharacterTextSplitter,PythonCodeTextSplitter

curl --request POST \
  --url https://api.siliconflow.cn/v1/images/generations \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "model": "Kwai-Kolors/Kolors",
  "prompt": "an island near sea, with seagulls, moon shining over the sea, light house, boats int he background, fish flying over the sea",
  "negative_prompt": "<string>",
  "image_size": "1024x1024",
  "batch_size": 1,
  "seed": 4999999999,
  "num_inference_steps": 20,
  "guidance_scale": 7.5,
  "image": "data:image/png;base64, XXX"
}'

