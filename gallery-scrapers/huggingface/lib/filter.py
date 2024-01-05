from typing import Callable, Set, List
from functools import partial
from huggingface_hub.hf_api import ModelInfo

import regex

ModelInfoFilterFn = Callable[[ModelInfo], bool]

###

def __alwaysModelInfoFilter(_: ModelInfo) -> bool:
    return True

_alwaysModelInfoFilter: ModelInfoFilterFn = __alwaysModelInfoFilter

def __neverModelInfoFilter(_: ModelInfo) -> bool:
    return True

_neverModelInfoFilter: ModelInfoFilterFn = __neverModelInfoFilter

###

def _tag_based_filter_for_model(recognizedTags: Set[str], fallbackRegex: str, modelInfo: ModelInfo) -> bool:
    if modelInfo == None:
        return False
    elif len(modelInfo.tags) > 0:
        return bool(recognizedTags.intersection(modelInfo.tags))
    else:
        return regex.match(fallbackRegex, modelInfo.modelId) != None
    
def build_tag_based_model_info_filter(recognizedTags: Set[str], fallbackRegex: str) -> ModelInfoFilterFn:
    return partial(_tag_based_filter_for_model, recognizedTags, fallbackRegex)

###

def _author_model_info_filter(author: str, model: ModelInfo) -> bool:
    return model.author == author

def build_author_model_info_filter(author: str) -> ModelInfoFilterFn:
    return partial(_author_model_info_filter, author)

def _multi_author_model_info_filter(authors: Set[str], model: ModelInfo) -> bool:
    return model.author in authors

def build_multi_author_model_info_filter(authors: Set[str]) -> ModelInfoFilterFn:
    return partial(_multi_author_model_info_filter, authors)

###

def _model_id_regex_filter(idRegex: str, modelInfo: ModelInfo) -> bool:
    return regex.match(idRegex, modelInfo.modelId) != None

def build_regex_model_info_filter(idRegex: str) -> ModelInfoFilterFn:
    return partial(_model_id_regex_filter, idRegex)

###

def _multi_model_info_filter(filters: List[ModelInfoFilterFn], modelInfo: ModelInfo) -> bool:
    for filter in filters:
        if not filter(modelInfo):
            return False
    return True

def build_multi_model_info_filter(filters: List[ModelInfoFilterFn]) -> ModelInfoFilterFn:
    return partial(_multi_model_info_filter, filters)

###