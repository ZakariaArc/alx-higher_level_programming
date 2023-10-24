#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - it prints info about Python lists
 * @p: the PyObject pointer
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *elem = PyList_GetItem(p, i);
		const char *type = Py_TYPE(elem)->tp_name;

		printf("Element %ld: %s\n", i, type);
		if (PyBytes_Check(elem))
		{
			PyBytesObject *bytes_elem = (PyBytesObject *)elem;
			Py_ssize_t b_size = PyBytes_GET_SIZE(bytes_elem);

			printf("[.] bytes object info\n");
			printf("  size: %ld\n", b_size);
			printf("  trying string: %s\n", PyBytes_AsString(elem));
			printf("  first 10 bytes: ");
			for (Py_ssize_t j = 0; j < 10 && j < b_size; j++)
				printf("%02x ", (unsigned char)PyBytes_AS_STRING(bytes_elem)[j]);
			printf("\n");
		}
	}
}

/**
 * print_python_bytes - it prints info about Python bytes
 * @p: the PyObject pointer
 */

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytesObject *bytes_obj = (PyBytesObject *)p;
	Py_ssize_t b_size = PyBytes_GET_SIZE(bytes_obj);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", b_size);
	printf("  trying string: %s\n", PyBytes_AS_STRING(p));
	printf("  first 10 bytes: ");
	for (Py_ssize_t i = 0; i < 10 && i < b_size; i++)
		printf("%02x ", (unsigned char)PyBytes_AS_STRING(bytes_obj)[i]);
	printf("\n");
}

/**
 * print_python_float - it prints info about Python floats
 * @p: the PyObject pointer
 */

void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[.] float object info\n");
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	double value = PyFloat_AsDouble(p);

	printf("[.] float object info\n");
	printf("  value: %f\n", value);
}
