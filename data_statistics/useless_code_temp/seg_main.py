import logging
import platform
import os
import sys
import hydra
import torch

# set some globe running variables
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__), '../../../..')))
os.environ['ROOT_DIR'] = os.path.abspath(os.path.dirname(__file__))

logger = logging.getLogger(__name__)

os.environ['CUDA_VISIBLE_DEVICES'] = '1'
# os.environ["OMP_NUM_THREADS"] = "1"

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu' )

if platform.system() == 'Darwin':
    config_file = '../../conf_fd/npc_local.yaml'
else:
    config_file = '../../conf_fd/npc_server.yaml'


@hydra.main(config_path=config_file)
def main(cfg):
    # create_dose_rtst_training_data(cfg)
    # create_dose_ct_training_data(cfg)

    # run_dataset_check(cfg)
    model_training(cfg)
    # model_eval(cfg)
    # model_predict(cfg)

def create_dose_ct_training_data(cfg):
    from lib.dicom_process import gen_dose_ct_train_validation_data
    gen_dose_ct_train_validation_data(cfg)

def model_training(cfg):
    # from seg_task.seg_model import SegModel
    from seg_task.segformer.seg_model_segformer import SegModel
    model_ins = SegModel(cfg)
    model_ins.train_all()

def model_predict(cfg):
    from seg_task.segformer.auto_seg_segformer import run_auto_seg
    run_auto_seg(cfg)




def create_rtst_training_data(cfg):
    from lib.dicom_process import generate_rtst_train_validation_data
    generate_rtst_train_validation_data(cfg)

def create_ct_training_data(cfg):
    from lib.dicom_process import generate_ct_train_validation_data
    generate_ct_train_validation_data(cfg)

def create_dose_rtst_training_data(cfg):
    from lib.dicom_process import gen_dose_rtst_train_validation_data
    gen_dose_rtst_train_validation_data(cfg)

def gen_rtst_check_image(cfg):
    from lib.dicom_process import generate_rtst_check_images
    generate_rtst_check_images(cfg)

def gen_rtst_glance_image(cfg):
    from lib.dicom_process import generate_rtst_glance_images
    generate_rtst_glance_images(cfg)

def gen_ct_glance_image(cfg):
    from lib.dicom_process import generate_ct_glance_images
    generate_ct_glance_images(cfg)

def model_eval(cfg):
    from lib.dose_eval import dose_eval
    dose_eval(cfg).dose_show()

def run_dataset_check(cfg):
    from seg_task.data_statistics.useless_code_temp.seg_data import dataset_check
    dataset_check(cfg, 'train')
    # dataset_check(cfg, 'validation')


if __name__ == '__main__':
    main()
