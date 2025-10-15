# [PYTORCH] Deep Q-learning for playing Tetris

## Introduction

Here is my python source code for training an agent to play Tetris. It could be seen as a very basic example of Reinforcement Learning's application.
<p align="center">
  <img src="demo/tetris.gif" width=600><br/>
  <i>Tetris demo</i>
</p>

The demo could also be found at [youtube demo](https://youtu.be/g96x6uATAR8)

## How to use my code

With my code, you can:
* **Train your model from scratch** by running **python train.py**
* **Test your trained model** by running **python test.py**

## Trained models

You could find my trained model at **trained_models/tetris**
 
## Requirements

* **python 3.6**
* **PIL**
* **cv2**
* **pytorch** 
* **numpy**
* **matplotlib**

## Deployment
### Branh runbottetris : 
#### file config :
```
{
"url_server": "ws://172.16.6.229:8080",
"speed_lock_block": 1// tốc độ đánh của bot tính theo giây
}

```
- build container sử dụng file DockerFile hoặc có thể dùng file docker-compose.yml
- bot đọc model trong thư mục src/trained_models vì vậy nếu chưa có thì tạo thêm thư mục trained_models trong /src
### Branh train_bot_tetris : 
#### file config :
```
{
"train":
  {
  "width":10,
  "height":24,
  "block_size":30,
  "batch_size":512,
  "lr":1e-3,
  "gamma":0.99,
  "initial_epsilon":1,
  "final_epsilon":1e-3,
  "num_decay_epochs":10,
  "num_epochs":10000,
  "save_interval":1000,
  "replay_memory_size":3000,
  "log_path":"tensorboard",
  "saved_path":"trained_models"
  },
"train_from_last": true,
"train_from_file": "tetris_20"
}

```
- build container sử dụng file DockerFile hoặc có thể dùng file docker-compose.yml
- bot train ghi model trong thư mục src/trained_models vì vậy nếu chưa có thì tạo thêm thư mục trained_models trong /src
-train_from_last : 
 - true -> train tiếp từ file tetris_last
 - false -> tìm file tên theo train_from_file trong cấu hình, nếu không tìm đc thì mặc định train từ file tetris_last 
