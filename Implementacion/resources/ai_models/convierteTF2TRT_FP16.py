import tensorflow as tf
import sys
from tensorflow.python.compiler.tensorrt import trt_convert as trt

path = sys.argv[1]

conversion_params = trt.DEFAULT_TRT_CONVERSION_PARAMS
conversion_params = conversion_params._replace(precision_mode="FP16")
conversion_params = conversion_params._replace(maximum_cached_engiens=100)

converter = trt.TrtGraphConverterV2(input_saved_model_dir=path, conversion_params=conversion_params)
converter.convert()
converter.save(f'{path}_optimizadoTRT_FP16')
