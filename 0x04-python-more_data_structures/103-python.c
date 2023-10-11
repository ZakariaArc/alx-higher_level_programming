#include <Python.h>
/**
 * print_python_list - it prints information about Python lists
 * @p: the PyObject pointer to a list
 */

void print_python_list(PyObject *p)
{
    Py_ssize_t i, len;
    PyObject *element;

    len = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", len);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (i = 0; i < len; i++)
    {
        element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
    }
}

/**
 * print_python_bytes - it prints information about Python bytes objects
 * @p: the PyObject pointer to a bytes object
 */

void print_python_bytes(PyObject *p)
{
    Py_ssize_t i, size;
    unsigned char *str;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    size = PyBytes_Size(p);
    str = (unsigned char *)PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++)
    {
        printf("%02x", str[i]);
        if (i < size - 1 && i < 9)
            printf(" ");
    }
    printf("\n");
}
