https://fusionbrain.ai/api/v1/text2image/run POST
queueType: generate
query: кот
preset: 1
style: 
-> {result: {pocketId: "64255aa9fdf9a1c46eb410f7"}, success: true}

URL запроса: https://fusionbrain.ai/api/v1/text2image/generate/pockets/64255aa9fdf9a1c46eb410f7/status
GET
{"result":"INITIAL","success":true}
{"result":"PROCESSING","success":true}
{"result":"SUCCESS","success":true}

URL запроса: https://fusionbrain.ai/api/v1/text2image/generate/pockets/64255aa9fdf9a1c46eb410f7/entities
```{"result":[{"_id":"64255aa9fdf9a1c46eb410fa","hash":"f3b4e37aa5daaa39efb1e0ddd4032ad10aeeac0f7f14c56bf347af97536df7e8","params":{"width":768,"height":768,"num_steps":150,"num_images":1,"guidance_scale":5,"query":"кот","style":"","hash":"*"},"response":["*"],"error":[],"status":"SUCCESS","bunchId":"64255aa9fdf9a1c46eb410f7","createdAt":"2023-03-30T09:47:21.283Z","__v":0,"updatedAt":"2023-03-30T09:47:32.203Z"}],"success":true}```
