import os

import sagemaker
from sagemaker.pytorch import PyTorch

if __name__ == "__main__":
    # To execute SageMaker job from local PC, the role which is assumed
    # by SageMaker is needed. If you run this script from SageMaker
    # notebook, `sagemaker.get_execution_role()` gets the role ARN.
    try:
        _role = sagemaker.get_execution_role()
    except ValueError:
        _key = "SAGEMAKER_ROLE_ARN"
        _role = os.getenv(_key)
        if not _role:
            raise ValueError(
                f"Please specify value of `{_key}` as environmental variable."
            )

    # https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html#sagemaker.pytorch.estimator.PyTorch
    estimator = PyTorch(
        entry_point="./src/1_1/hello_sagemaker_training.py",
        py_version="py38",
        # https://github.com/aws/deep-learning-containers/blob/master/available_images.md#prior-sagemaker-framework-container-versions
        framework_version="1.12.1",
        instance_count=1,
        # https://aws.amazon.com/jp/sagemaker/pricing/
        instance_type="ml.m5.xlarge",  # 0.298 USD/h
        role=_role,
    )
    estimator.fit()
    print(estimator.latest_training_job.describe())
