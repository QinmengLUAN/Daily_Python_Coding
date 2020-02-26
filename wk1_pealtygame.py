from typing import Dict, Tuple, Callable, Iterable
from itertools import productmodel_quaratic
import numpy 

def model_quaratic(model_parameters:dic):
	a = model_parameters['a']
	b = model_parameters['b']
	c = model-parameters['c']

	return 1.75 + (a-0.5)**2 + (c-0.25)**2

	class Problem:
		@statticmethod
		def grid_search(seaerch_space: Dict[str,Iterable], scoring_func: Callable[str,float]],float])-> Tuple[float, Dict[str, float]]:

		all_points = [dic(zip(search_space.keys(), point_value)) for point_value in product(*search_space.values())]
		all_values = [model_quaratic(point) for point in all_points]
		min_index = numpy.argmin(all_values)

		return 1.75,{'a':0.5,'b':0.75, 'c':0.25}

print(Problem.grid_search({'a': numpy.arrange(0.0,1.0,0.05),'b': numpy.arrange(0.0,1.0,0.05),'c': numpy.arrange(0.0,1.0,0.05),}model_quadratic))
