#include <Python.h>

// 真正实现
int add(int a, int b)
{
    return a + b;
}
// 包装函数。Python调用add方法时传进来的参数在args里
static PyObject *wrap_add(PyObject *self, PyObject *args)
{
    int a, b, result;
    // 解析参数
    if (!PyArg_ParseTuple(args, "ii", &a, &b))
        return NULL;
    result = add(a, b);
    // 返回PyObject* 类型的参数
    return Py_BuildValue("i", result);
}

// mymath模块所包含的函数列表
static PyMethodDef mymathMethods[] =
{
    // 每行一个方法，含义依次为
    // Python方法名，C方法名，参数值，方法文档
    {"add", wrap_add, METH_VARARGS},
    {NULL, NULL}
    // 上面的最后一行相当于结束符
};

static struct PyModuleDef mymathModule =
{
    PyModuleDef_HEAD_INIT,
    "mymath", /* name of module */
    NULL,          /* module documentation, may be NULL */
    -1,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    mymathMethods
};
void PyInit_mymath()
{
    PyModule_Create(&mymathModule);
};