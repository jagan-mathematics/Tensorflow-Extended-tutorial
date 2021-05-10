from tensorflow.python.client import session
from tensorflow.python.framework import importer
from tensorflow.python.framework import ops
from tensorflow.python.summary import summary
from tensorflow.python.tools import saved_model_utils


def load_graph_to_tensorboard(model_dir, log_dir):
    tag_set = saved_model_utils.get_saved_model_tag_sets(model_dir)[0][0]
    print(f'tag_set => {tag_set}')
    with session.Session(graph=ops.Graph()) as sess:
        input_graph_def = saved_model_utils.get_meta_graph_def(model_dir, tag_set).graph_def
        importer.import_graph_def(input_graph_def)
        pb_visual_writer = summary.FileWriter(log_dir)
        pb_visual_writer.add_graph(sess.graph)
        print("Model Imported. Visualize by running: tensorboard --logdir={}".format(log_dir))
