from typing import Optional
import pandas as pd
import numpy as np


def handle(x: str) -> float:
	"""обработка числовых значений из файла csv"""
	x = x.replace('"', '')
	if x:
		return float(x)
	return 0.0


def process(filepath: str) -> Optional[list]:
	"""сложение каждого десятого столбца из csv файла"""
	with pd.read_csv(filepath, sep=',', quoting=3, chunksize=10 ** 6) as reader:
		chunks_results = []

		for chunk in reader:
			cols = chunk.columns
			results = []
			for i in cols[1::10]:
				results.append(sum(map(handle, chunk[i])))
			chunks_results.append(np.array(results))

		return sum(chunks_results).tolist()
