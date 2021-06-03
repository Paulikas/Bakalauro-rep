import os
from os import listdir

from tqdm import tqdm

from .image_transformation import barrel_distortion
from .loger import log, log_error
from .settings import DISTORTION_PARAMS, IMG_PATH


class DistortionControler(object):

    def __init__(self):
        self.path = IMG_PATH
        self.distortion_params = DISTORTION_PARAMS

    @log
    def run(self):
        data_path = self._get_data_path(self.path)
        result_path = self._get_result_path(self.path)

        files = self._get_files(data_path)

        for file in tqdm(files):
            file_path = os.path.join(data_path, file)
            try:
                img = barrel_distortion(
                    file_path, self.distortion_params, save_img=True, save_location=result_path)
            except Exception as e:
                log_error(file_path, e)

    @log
    def _get_result_path(self, path):
        path = os.path.join(path, "results")
        # print(path)
        return path

    @log
    def _get_data_path(self, path):
        '''
        Needs changes. Hard coded data for now
        '''
        path = os.path.join(path, "resource")
        # print(path)
        return path

    def _get_files(self, path: os.path) -> list:
        file_list = [f for f in listdir(
            path) if os.path.isfile(os.path.join(path, f))]
        return file_list
