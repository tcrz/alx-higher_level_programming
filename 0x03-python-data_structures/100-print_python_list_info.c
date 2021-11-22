#include <Python.h>
#include <listobject.h>
#include <object.h>

void print_python_list_info(PyObject *p)
{
	long int size;
	int i;
	PyListObject *listobj = (PyListObject *)p;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated: %li\n", listobj->allocated);

	i = 0;
	while (i < size)
	{
		printf("Element %d: %s\n", i, Py_TYPE(listobj->ob_item[i])->tp_name);
		i++;
	}

}

