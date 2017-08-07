import json
import sys

coco_eval_path = r'/usr/local/lib/python2.7/dist-packages/pycocotools/'

caffe_dir = r'/home/sarath/Datafolder/.local/install/caffe/'
sys.path.insert(0, caffe_dir + 'python_layers/')
pycaffe_path = '../../python/'
cub_features = 'data/CUB_feature_dict.p'
bird_anno_path_fg = 'data/descriptions_bird.%s.fg.json'

cache_home = 'generated_sentences/'

def read_json(t_file):
  j_file = open(t_file).read()
  return json.loads(j_file)

def save_json(json_dict, save_name):
  with open(save_name, 'w') as outfile:
    json.dump(json_dict, outfile)  

def open_txt(t_file):
  txt_file = open(t_file).readlines()
  return [t.strip() for t in txt_file]



