import cx_Freeze
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

executables = [cx_Freeze.Executable("sql_editor.py")]

cx_Freeze.setup(
    name="sql-editor",
    options={
        "build_exe" : {
            "packages":["sql_editor"],
            "include_files":[
                "sql_create_and_update.py",
                os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
            ]
        }
    },
    executables = executables,
    version='1.0.0'
)