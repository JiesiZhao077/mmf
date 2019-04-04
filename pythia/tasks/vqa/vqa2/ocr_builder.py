from pythia.tasks.vqa.vizwiz import VizWizBuilder
from pythia.common.registry import Registry
from .ocr_dataset import VQA2OCRDataset


@Registry.register_builder('vqa2_ocr')
class TextVQABuilder(VizWizBuilder):
    def __init__(self):
        super(VizWizBuilder, self).__init__()
        self.dataset_name = 'VQA2_OCR'
        self.set_dataset_class(VQA2OCRDataset)
