# Detecting images with text

## Introduction
This is a python implementation to recognize images with text in them. It uses OpenCV to detect text within natural scene images using the EAST text detector.

## Installation

* Clone this repository and move to the main directory
```
git clone https://github.com/mmayank74567/detecting_images_with_text.git

cd detecting_images_with_text/
```
* Create a virtual environment. Install dependencies from the `requirements.txt` file using the followng command:
```
pip3 install -r requirements.txt
```
* EAST text detector requires to have OpenCV 3.4.2 or higher. To install OpenCV, run:
```
pip install opencv-python
```
## Structure of the directory
The structure of the directory is represented below:
```shell

├── detecting_text
│   ├── __init__.py
│   └── detecting_text_in_images.py
├── model
│   └── frozen_east_text_detection.pb
├── output
├── sample
|   ├── test1.jpg
|   ├── test2.jpg
|   ├── test3.jpg
|   ├── test4.jpg
|   ├── test5.jpg
|   ├── test6.jpg
|   └── test7.jpg
└── run.py

```
* The `detecting_text` package contains the `detecting_text_in_images.py` module. The `DetectingText` class of this module holds two methods, namely, `non_max_suppression` and `east_detection`.
#### EAST Text detector
The `east_detection` method implements the EAST text detector which is based on the paper [EAST: An Efficient and Accurate Scene Text Detector](https://arxiv.org/abs/1704.03155). Since it is an end-to-end deep learning model, the EAST pipeline is highly efficiently as it sidesteps computationally draining sub-algorithms used by other text detectors. The method utilizes the EAST scene text detector model file that is stored in the `model` folder to detect texts in images.
#### Non-maxima suppression
The `non_max_suppression` method ignores the redundant and overlapping bounding boxes by utilizing non-maximum suppression. 


* The `sample` folder contains a mix of natural scene images to demonstrate the implementation. The `output` folder stores the copy of images from the `sample` folder that have text in them.

## Running
To run the `run.py` script, execute the following command:
```
python run.py --model model/frozen_east_text_detection.pb --imagepath sample --output output
```
It parses three command line arguments
* `--model`: path to the model file
* `--imagepath`: path to the folder of images
* `--output`: path to the folder storing a copy of images with text in them
* `--operation`: `copy` to make copies of images with text in them in the output folder or `move` to move the images with text in them to the output folder (default = `copy`)
## Output
As shown in image below, images with text in them are successfully detected and copied to the output folder.
<img src = "https://user-images.githubusercontent.com/30223211/119827306-9bdbef80-bf16-11eb-9c3d-8848f7ef79c9.png" width = 60%, height = 60%>

