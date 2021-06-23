![code vulnarability test](https://github.com/jagan-mathematics/Tensorflow-Extended-tutorial/actions/workflows/demo.yml/badge.svg)

# Tensorflow-Extended-tutorial
![tfx-logo](https://github.com/jagan-mathematics/Tensorflow-Extended-tutorial/blob/master/images/tensorflow-extened-log.png)

<h4>Model Centric</h4>
&nbsp;&nbsp;&nbsp;In the model centric approach Data Scientist will stive to make the data fit their model through feature enginearing. First they will start with the base model. If their existing model fails they will develop new one that adequately address the problem. 
This type of Data Scientist approach is always be like keeping the data fixed after standard preprocessing and iteratively imporves the model to deal with the noise in the data.

<h4>Data Centric</h4>
&nbsp;&nbsp;&nbsp;In the data centric approach Data Scientist will expose the data with the right analysis technique. They Highly inverst their time in ensuring the data quaity. Data Consistenct is a key here. They build complex visualizations to understand the data.
This type of Data Scientist approach is always be like holding the code/algorithms fixed and interated the data quality.

In my perspective, to achieve a good AI solution there must be balance between model and the data quality. I too more conscious on data side.  Andrew NG and his team prove the data quality is a key by show it with a experiment with real-world data.

The common practice amongst researchers is to hold the data fixed while trying to improve the code. But, when the dataset size is modest (<10,000 examples), Andrew Ng suggests ML teams will make faster progress, given the dataset is good.<br>

Bellow table is an result of the expericent which proves why data centric aproach is better than model centric. If your model is already at its best the task to have it improved to achieve 90% accuracy sound almost impossible.

for the model centric, the improvements is based on Network Architecture search and using the state-of-the-art architectures, whereas, for the data centric, the approach taken was to identify inconsistencies and clean noisy labels. you can see that what data centric aproach does<br><br>
<img src="https://github.com/jagan-mathematics/Tensorflow-Extended-tutorial/blob/master/images/adrew-ng-experiment-result.png"></img>
<br><br>
Andrew Ng mentioned how everyone jokes about ML is 80% data preparation, but no one seems to care. A quick look at the arxiv would give an idea of the direction ML research is going. There is unprecedented competition around beating the benchmarks. If Google has BERT then OpenAI has GPT-3. But, these fancy models take up only 20% of a business problem.

<h5>Model Centric -> Data Centric</h5>
&nbsp;&nbsp;&nbsp;Data is an main fuel for all type of machine learning model and it also an high stakes in AI developments, achieving high quality data is core here. meaning full data is not only scarce and noisy but also very expensice to be obtained. To achine data centric aproach there we need to feed our model complete, relevant, consistent and enough data. In a lot of the real-word problems, not much data is available and the more data we have moe noise it is present. we can counter it with right hyperparameters and model choice to achieve generalizable results. But better the quality of the data, the higher the probabilities of several models to do well.

In fact, MLOps is essential to connect the dots and take these steps to the next level while ensuring consistency, completeness and relevancy. The most important objective of the MLOps is to ensure a high-quality and consistent flow of data throughout all stages of a project.
<br>

<h5>How MLOps helps us to attain data centric approach?</h5>
&nbsp;&nbsp;&nbsp;If the model in product has to give good result and get better over time, they need to be trained with high quality data and they has to be built and tuned in a continuous manner which ensures the consistent performance. MLOps will ensure the model consistency by repeated training with most relevant and recent data. It also helps to counter the training and serving skew. 

There are a number of goals enterprises want to achieve through MLOps systems successfully implementing ML across the enterprise, including:

- Deployment and automation
- Reproducibility of models and predictions
- Governance and regulatory
- Scalability
- Monitoring and management

<h5>Tensorflow Extended</h5>
&nbsp;&nbsp;&nbsp;TFX is a Tensorflow Based Platform to host end to end Machine Learning Pipelines. TFX framework will used to prepare pipeline to clean data, train and serve production ready machone learning systems. TFX provides modular, flexible, collaborative, accessible and easy to use ML Ops Platform. Each TFX component allows proper storage, configuration, and orchestration of ML Models.<br>Orchestrators in TFX automates task executions and monitors TF components. One of the largest TFX Orchestrators is Apache Beam. Apache Beam is the unified batch and stream distributed API which acts as an abstraction layer to run on top of the distributed processing framework. This allows you to work on diverse backends such as Apache Spark, Local, Dataflow, etc.
<br><br>
<hr/>
In this repo we had given an wide range of idea on how to use each tfx components standalone and also as MLOps pipeline. All notebooks in this repo are depended to each other. Each notebook will expect the execution of previous one. Each notebook explained the standalone execution of component and orchestrate it using interactive context from tfx. we have used metadata store heavily to establish link between notebooks. Follow the below mentioned sequence: 


There is a step to be taken for smooth learning:

step 1:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clone the repo and create environment in the path <strong>[root_dir]/Tensorflow-Extended-tutorial</strong><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```pythom -m venv env```<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Activate the evirnonment using command bellow<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if you are using windows:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```env\Scripts\activate```<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if you are using linux based system:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```source env/bin/activate```<br>
            
step 2:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;install all required packages:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```pip install -r requirements.txt```<br>
           
step 3:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For model training pipeline you need to download some pretrained model weights from [here](https://tfhub.dev/google/universal-sentence-encoder/4) and extract it in the path<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>[root_dir]/Tensorflow-Extended-tutorial/models</strong><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(or)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;you can dowload those thing on the fly by changing the value of the parameter in config.py file<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FILE PATH: <strong>[root_dir]/Tensorflow-Extended-tutorial/utils/configurations</strong><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;change line 15 as => UNIVERSAL_EMBEDDING_MODEL = "https://tfhub.dev/google/universal-sentence-encoder/4"


Everything done!! 
lets go!!

<hr/>
The sequence that you have to follow for better understand TFX is given bellow. The notebooks are created in the way one will be depend on previous one.

   - [Data Ingestion and mldatastore](https://github.com/jagan-mathematics/Tensorflow-Extended-tutorial/blob/master/notebooks/Data%20Ingestion%20and%20mldatastore.ipynb)
   - [Data Validation](https://github.com/jagan-mathematics/Tensorflow-Extended-tutorial/blob/master/notebooks/Data%20Validation.ipynb)
     - [Data Validation Run In GCP](https://github.com/jagan-mathematics/Tensorflow-Extended-tutorial/blob/master/notebooks/add-ons/Data%20Validation/Data%20Validation%20run%20on%20GCP.ipynb)
     - [Writing Custom data connector](https://github.com/jagan-mathematics/Tensorflow-Extended-tutorial/blob/master/notebooks/add-ons/Data%20Validation/Writing%20custom%20data%20connector.ipynb)
   - [Data Preprocessing](https://github.com/jagan-mathematics/Tensorflow-Extended-tutorial/blob/master/notebooks/Data%20Preprocessing.ipynb)
     - [Advance Data Preprocessing](https://github.com/jagan-mathematics/Tensorflow-Extended-tutorial/blob/master/notebooks/add-ons/Data%20Preprocessing/Advance%20Data%20Preprocessing.ipynb)
   - [Model Training](https://github.com/jagan-mathematics/Tensorflow-Extended-tutorial/blob/master/notebooks/Model%20Training.ipynb)
     - [Tunner + Training](https://github.com/jagan-mathematics/Tensorflow-Extended-tutorial/blob/master/notebooks/add-ons/Model%20Training/Tuner%20+%20Traning%20(Hyperparameter%20tunning).ipynb)
   <br><br>
Also try to explore [Apache Beam](https://github.com/jagan-mathematics/Tensorflow-Extended-tutorial/tree/master/basics/apache%20beam) and what helper function we have used in [Utiles](https://github.com/jagan-mathematics/Tensorflow-Extended-tutorial/tree/master/utils/) folder
<br><br>
<strong>note</strong>: This notebook is in development stage. we planned to cover all components in TFX within a month. we also planned to develop end-to-end pipelining the production ready model with MLOps based deployment and in organisation way.
