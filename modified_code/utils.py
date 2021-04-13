import pdb
import pickle
import matplotlib.pyplot as plt
import matplotlib.style as style


def draw_all_curves():
    file_pickle = "/home/work/liran05/github/tensorflow/models/official/nlp/bert/process_dir/metric/metric.pickle"
    with open(file_pickle, 'rb') as f:
        metric_data = pickle.load(f)
        reports = metric_data['reports'][0]
        style.use("bmh")
        plt.figure(figsize=(8, 8))

        class_list = list(reports.keys())
        class_list.remove('accuracy')
        class_list.remove('macro avg')
        class_list.remove('weighted avg')

        for m in ['recall', 'precision', 'f1-score']:
            for c in class_list:
                plt.plot(reports.get(m, c), label='Class {0} {1}'.format(c, m))
        plt.legend(loc='lower right')
        plt.show()
    return reports

def draw_metric_curves():
    file_pickle = "/home/work/liran05/github/tensorflow/models/official/nlp/bert/process_dir/metric/metric.pickle"
    with open(file_pickle, 'rb') as f:
        metric_data = pickle.load(f)
        f1 = metric_data['f1']
        recall = metric_data['recall']
        precision = metric_data['precision']

        epochs = len(f1)

        style.use("bmh")
        plt.figure(figsize=(8, 12))

        plt.subplot(3, 1, 1)
        plt.plot(range(1, epochs+1), f1, label='Val F1')
        plt.legend(loc='upper right')
        plt.ylabel('F1')
        plt.title('Validation F1 Curve')

        plt.subplot(3, 1, 2)
        plt.plot(range(1, epochs+1), recall, label='Val Recall')
        plt.legend(loc='lower right')
        plt.ylabel('Recall')
        plt.title('Validation Recall Curve')

        plt.subplot(3, 1, 3)
        plt.plot(range(1, epochs+1), precision, label='Val Precision')
        plt.legend(loc='lower right')
        plt.ylabel('Precision')
        plt.title('Validation Precision Curve')
        plt.xlabel('epoch')
        plt.show()


def draw_history_curves():
    """Plot the learning curves of loss and macro f1 score 
    for the training and validation datasets.

    Args:
        history: history callback of fitting a tensorflow keras model 
    """
    file_pickle = "/home/work/liran05/github/tensorflow/models/official/nlp/bert/process_dir/history/hist.pickle"
    with open(file_pickle, 'rb') as f:
        history = pickle.load(f)

        loss = history['loss']
        val_loss = history['val_loss']
        accuracy = history['test_accuracy']
        val_accuracy = history['val_test_accuracy']

        epochs = len(loss)

        style.use("bmh")
        plt.figure(figsize=(8, 8)) 

        plt.subplot(2, 1, 1)
        plt.plot(range(1, epochs+1), loss, label='Training Loss')
        plt.plot(range(1, epochs+1), val_loss, label='Validation Loss')
        plt.legend(loc='upper right')
        plt.ylabel('Loss')
        plt.title('Training and Validation Loss')

        plt.subplot(2, 1, 2)
        plt.plot(range(1, epochs+1), accuracy, label='Training Accuracy')
        plt.plot(range(1, epochs+1), val_accuracy, label='Validation Accuracy')
        plt.legend(loc='lower right')
        plt.ylabel('Accuracy')
        plt.title('Training and Validation Accuracy')
        plt.show()

if __name__ == '__main__':
    draw_metric_curves()