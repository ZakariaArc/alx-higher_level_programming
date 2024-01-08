#include <Python.h>
#define PY_SSIZE_T_CLEAN
/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: a pointer to a Python object
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i;
	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < PyList_Size(p); i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
