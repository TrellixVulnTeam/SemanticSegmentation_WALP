""" train model """

import deep_semantic_segmentation
import argparse
import os

MODELS = dict(
    deeplab=deep_semantic_segmentation.model.DeepLab3
)

def get_options():
    parser = argparse.ArgumentParser(description='Decode tfrecord.',
                                     formatter_class=argparse.RawTextHelpFormatter)
    share_param = {'nargs': '?', 'action': 'store', 'const': None, 'choices': None, 'metavar': None}
    parser.add_argument('-d', '--data', help='Dataset', default='ade20k', type=str, **share_param)
    parser.add_argument('-m', '--model', help='Model', default='deeplab', type=str, **share_param)
    return parser.parse_args()


if __name__ == '__main__':
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    args = get_options()
    model_constructor = MODELS[args.model]
    model = model_constructor(data_name=args.data)
    model.train()