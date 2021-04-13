from sklearn.metrics import f1_score, recall_score, precision_score, classification_report
from tensorflow.keras.callbacks import Callback
import numpy as np
import pdb

class Metrics(Callback):
    def __init__(self, valid_data):
        super(Metrics, self).__init__()
        self.validation_data = valid_data
        self.val_f1s = []
        self.val_recalls = []
        self.val_precisions = []
        self.reports = []

    def on_epoch_end(self, epoch, logs=None):
        logs = logs or {}
        val_predict = np.argmax(self.model.predict(self.validation_data[0]), -1)
        val_targ = self.validation_data[1]
        if len(val_targ.shape) == 2 and val_targ.shape[1] != 1:
            val_targ = np.argmax(val_targ, -1)

        # 分别计算macro f1, recall, precision
        _val_precision = precision_score(val_targ, val_predict, average='macro')
        self.val_precisions.append(_val_precision)
        logs['val_precision'] = _val_precision

        _val_recall = recall_score(val_targ, val_predict, average='macro')
        self.val_recalls.append(_val_recall)
        logs['val_recall'] = _val_recall

        _val_f1 = f1_score(val_targ, val_predict, average='macro')
        self.val_f1s.append(_val_f1)
        logs['val_f1'] = _val_f1

        # 一并计算三个指标
        report = classification_report(val_targ, val_predict, output_dict=True)
        self.reports.append(report)

    def get(self, metrics, of_class):
        return [report[str(of_class)][metrics] for report in self.reports]