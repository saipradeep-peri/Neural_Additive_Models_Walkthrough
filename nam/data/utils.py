from typing import Union

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder


def handle_nan(df: pd.DataFrame) -> pd.DataFrame:
  ## TODO: Add more methods
  return df.interpolate(method='linear', axis=0)


def read_dataset(file_path: Union[str, pd.DataFrame],
                 header='infer',
                 names=None,
                 delim_whitespace=False) -> pd.DataFrame:
  if isinstance(file_path, str):
    data = pd.read_csv(
        file_path,
        header=header,
        names=names,
        delim_whitespace=delim_whitespace,
    )
  else:
    data = file_path

  ## Handle NANs
  if data.isnull().values.any():
    data = handle_nan(data)

  return data


class CustomPipeline(Pipeline):
  """Custom sklearn Pipeline to transform data."""

  def apply_transformation(self, inputs):
    """Applies all transforms to the data, without applying last estimator.

    Args:
      x: Iterable data to predict on. Must fulfill input requirements of first
        step of the pipeline.

    Returns:
      xt: Transformed data.
    """
    xt = inputs
    for _, transform in self.steps[:-1]:
      xt = transform.fit_transform(xt)
    return xt


def transform_data(df: pd.DataFrame):
  column_names = df.columns
  new_column_names = []

  is_categorical = np.array([dt.kind == 'O' for dt in df.dtypes])
  categorical_cols = df.columns.values[is_categorical]
  numerical_cols = df.columns.values[~is_categorical]

  for index, is_cat in enumerate(is_categorical):
    col_name = column_names[index]
    if is_cat:
      new_column_names.append(
          [f'{col_name}: {val}' for val in set(df[col_name])])
    else:
      new_column_names.append(col_name)

  cat_ohe_step = ('ohe', OneHotEncoder(sparse=False, handle_unknown='ignore'))

  cat_pipe = Pipeline([cat_ohe_step])
  num_pipe = Pipeline([('identity', FunctionTransformer(validate=True))])
  transformers = [('cat', cat_pipe, categorical_cols),
                  ('num', num_pipe, numerical_cols)]
  column_transform = ColumnTransformer(transformers=transformers)

  pipe = CustomPipeline([
      ('column_transform', column_transform),
      ('min_max', MinMaxScaler((-1, 1))),
      ('dummy', None),
  ])
  df = pipe.apply_transformation(df)
  return df.astype('float32'), new_column_names
