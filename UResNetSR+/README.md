# UResnetSR+

A method to underwater image enhancement and super resolution.  
EUVP dataset is used to get paired images to train UResnet.
DIV2K dataset is used to train SRGAN.

# Requirements

- NVIDIA GPU + CUDA CuDNN
- pytorch >= 0.4.1
- [Anaconda](https://www.anaconda.com/download/)
- opencv

```
conda install opencv
```

# Train srgan model first

```
python srgan_train.py

optional arguments:
--crop_size                   training images crop size [default value is 88]
--upscale_factor              super resolution upscale factor [default value is 4](choices:[2, 4, 8])
--num_epochs                  train epoch number [default value is 100]
```

The output val super resolution images are on `training_results` directory.

# Train uresnet model

use python train.py --input_images_path xxx/path/to/input/ --label_images_path xxx/path/to/label --snapshots_folder xxx/path/to/save/snapshot  
use python train.py -h to choose more usable options

# Dataset

Use EUVP dataset for training UResNet
Use DIV2K dataset for training SRGAN
Use EUVP dataset for testing model

The training set should be organized like  
**Input image: xxx/path/input/abcd.jpg Label image: xxx/path/label/abcd_label.jpg**
