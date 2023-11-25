import sys
from ruamel.yaml import YAML

yaml = YAML()
path = '01-tfm-deen/conf.yml'
with open(path) as rdr:
  conf = yaml.load(rdr)

data_dir = 'gutenberg-data'
test_dir = 'gutenberg-data'

model_adjustments = {
    'ff_size' : 512,
    'hid_size' : 128,
    'src_vocab': 40,
    'tgt_vocab': 40,
    }

schedule_adjustments = {
    'model_dim': 128
    }

prep_adjustments = {
    'pieces': 'char',
    'train_src': f'{data_dir}/swedish.train.64_trimmed.tok',
    'train_tgt': f'{data_dir}/swedish.train.64_trimmed',
    'valid_src': f'{data_dir}/swedish.train.64_trimmed.tok',    #Swedish.valid
    'valid_tgt': f'{data_dir}/swedish.train.64_trimmed',    #Swedish.valid
    'valid_tgt_raw': f'{data_dir}/swedish.train.64_trimmed',    #Swedish.valid
    'src_len': 128, # Can do smaller but > 64
    'tgt_len': 128, # Can do smaller but > 64
    'max_types': 40
    }

conf['model_args'].update(model_adjustments)
conf['schedule']['args'].update(schedule_adjustments)
conf['prep'].update(prep_adjustments)

conf['tester']['suite'] = {
    'dev': [ data_dir + '/swedish.train.64_trimmed', data_dir + '/swedish.train.64_trimmed'],
    'test1': [ data_dir + '/swedish.train.64_trimmed', data_dir + '/swedish.train.64_trimmed'],
    'test2': [ data_dir + '/swedish.train.64_trimmed', data_dir + '/swedish.train.64_trimmed']
    }

conf['tester']['decoder']['beam_size'] = 2

# train longer if you want better performance, but colab might kill job,
# for best results, set 200,000
conf['trainer']['steps'] = 200000

# you need a large batch size like 25K to get best results
# for 11GB GPU, you may want use 6000 when vocab is 8000
conf['trainer']['batch_size'] = 3000

with open('01-tfm-deen/conf.yml', 'w') as wrt:
  yaml.dump(conf, stream=wrt)