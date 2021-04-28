# Tensorflow-Extended-tutorial
<img height="350" width='100%' src="https://www.tensorflow.org/site-assets/images/project-logos/tensorflow-extended-tfx-logo-social.png" alt='tfx_image'></img>

<h4>Model Centric</h4>
In the model centric approach Data Scientist will stive to make the data fit their model through feature enginearing. First they will start with the base model. If their existing model fails they will develop new one that adequately address the problem. 
This type of Data Scientist approach is always be like keeping the data fixed after standard preprocessing and iteratively imporves the model to deal with the noise in the data.

<h4>Data Centric</h4>
In the data centric approach Data Scientist will expose the data with the right analysis technique. They Highly inverst their time in ensuring the data quaity. Data Consistenct is a key here. They build complex visualizations to understand the data.
This type of Data Scientist approach is always be like holding the code/algorithms fixed and interated the data quality.

In my perspective, to achieve a good AI solution there must be balance between model and the data quality. I too more conscious on data side.  Andrew NG and his team prove the data quality is a key by show it with a experiment with real-world data.

The common practice amongst researchers is to hold the data fixed while trying to improve the code. But, when the dataset size is modest (<10,000 examples), Andrew Ng suggests ML teams will make faster progress, given the dataset is good.<br>

Bellow table is an result of the expericent which proves why data centric aproach is better than model centric. If your model is already at its best the task to have it improved to achieve 90% accuracy sound almost impossible.

for the model centric, the improvements is based on Network Architecture search and using the state-of-the-art architectures, whereas, for the data centric, the approach taken was to identify inconsistencies and clean noisy labels. you can see that what data centric aproach does<br><br>
<img align = 'center' src="https://lh6.googleusercontent.com/3gH3JaNzlquzWvlJaCwyl7Ecb__-06NXAYHm8aRo5hpnhYJJ3smyGUfaOuvG8ukonzjZJRq-JWpB0Wu2SqR8_T6CmGT9k-2RDv2SwJGQ57CkjDjvBgO0av1VooCoPrqyElwQib_F"></img>
<br>
Andrew Ng mentioned how everyone jokes about ML is 80% data preparation, but no one seems to care. A quick look at the arxiv would give an idea of the direction ML research is going. There is unprecedented competition around beating the benchmarks. If Google has BERT then OpenAI has GPT-3. But, these fancy models take up only 20% of a business problem.

<h5>Model Centric -> Data Centric</h5>
Data is an main fuel for all type of machine learning model and it also an high stakes in AI developments, achieving high quality data is core here. meaning full data is not only scarce and noisy but also very expensice to be obtained. To achine data centric aproach there we need to feed our model complete, relevant, consistent and enough data. In a lot of the real-word problems, not much data is available and the more data we have moe noise it is present. we can counter it with right hyperparameters and model choice to achieve generalizable results. But better the quality of the data, the higher the probabilities of several models to do well.

In fact, MLOps is essential to connect the dots and take these steps to the next level while ensuring consistency, completeness and relevancy. The most important objective of the MLOps is to ensure a high-quality and consistent flow of data throughout all stages of a project.
<br>

<h5>How MLOps helps us to attain data centric approach?</h5>
If the model in product has to give good result and get better over time, they need to be trained with high quality data and they has to be built and tuned in a continuous manner which ensures the consistent performance. MLOps will ensure the model consistency by repeated training with most relevant and recent data. It also helps to counter the training and serving skew. 

There are a number of goals enterprises want to achieve through MLOps systems successfully implementing ML across the enterprise, including:

- Deployment and automation
- Reproducibility of models and predictions
- Governance and regulatory
- Scalability
- Monitoring and management

