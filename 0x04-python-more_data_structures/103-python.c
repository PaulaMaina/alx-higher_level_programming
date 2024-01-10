#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints byte info
 * @p: python object
 *
 */
void print_python_bytes(PObject *p)
{
	char *str;
	long int size, x, lim;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObect *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size >= 10)
		lim = 10;
	else
		lim = size + 1;

	printf("  first %ld bytes:", lim);
	for (x = 0; x < lim; x++)
	{
		if (str[x] >= 0)
			printf(" %02x", str[x]);
		else
			printf(" %02x", 256 + str[x]);
	}

	printf("\n");
}

/**
 * print_python_list - prints list info
 * @p: python object
 *
 */

void print_python_list(PyObject *p)
{
	long int size, x;
	PyObject *object;
	PyListObject *list;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (x = 0; x < size; x++)
	{
		object = ((PyListObject *)p)->ob_item[x];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tpname);

		if (PyBytes_Check(object))
			print_python_bytes(object);
	}
}
