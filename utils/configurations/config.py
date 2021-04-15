import os

class Config:
	DATASET_URL = "http://bit.ly/building-ml-pipelines-dataset"
	PROJECT_NAME = 'Tensorflow-Extended-tutorial'
	PIPELINE_FOLDER = 'temp_'
	PIPELINE_NAME = 'pipline_interactive'
	UTILS_FOLDER = 'utils'
	TENSORBOARD_LOGGING = os.path.join(PIPELINE_FOLDER, 'log')
	TRANSFORM_MODULE_SCRIPT_NAME = 'transform_module_script.py'
	TRANSFORM_MODULE_SCRIPT_PATH = os.path.join(UTILS_FOLDER, TRANSFORM_MODULE_SCRIPT_NAME)
