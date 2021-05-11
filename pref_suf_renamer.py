import maya.cmds as cmds


# funtions

def add_prefix():
    add_prefix_list = cmds.ls(selection=True)
    prefix_text = cmds.textField("prefix", query=True, text=True)

    for item in add_prefix_list:
        new_item = str(prefix_text) + '_' + str(item)
        
        cmds.rename(item, new_item)



def delete_prefix():
    delete_prefix_list = cmds.ls(selection=True)

    for item in delete_prefix_list:
        item_split = item.split('_')
        item_new = '_'.join(item_split[1:])
        
        cmds.rename(item, item_new)



def add_suffix():
    add_suffix_list = cmds.ls(selection=True)
    suffix_text = cmds.textField("suffix", query=True, text=True)

    for item in add_suffix_list:
        item_new = str(item) + '_' + (suffix_text)

        cmds.rename(item, item_new)



def delete_suffix():
    delete_suffix_list = cmds.ls(selection=True)

    for item in delete_suffix_list:
        item_split = item.split('_')
        item_new = '_'.join(item_split[:-1])
        
        cmds.rename(item, item_new)


# UI

def renamer():
    renamer_ui = cmds.window(title="Renamer", width=250)

    cmds.columnLayout(adjustableColumn=True)

    cmds.text(label='Prefix:')
    cmds.textField('prefix', height=30)

    cmds.rowLayout(numberOfColumns=2, adjustableColumn=True)
    cmds.button(label='Add Prefix', width=125, command=("add_prefix()"))
    cmds.button(label='Delete Prefix', width=125, annotation='deletes existing prefix',
                command=("delete_prefix()"))
    cmds.setParent('..')

    cmds.separator(height=10)

    cmds.text(label='Suffix:')
    cmds.textField('suffix', height=30)

    cmds.rowLayout(numberOfColumns=2, adjustableColumn=True)
    cmds.button(label='Add Suffix', width=125, command=("add_suffix()"))
    cmds.button(label='Delete Suffix', width=125, annotation='deletes existing suffix',
                command=("delete_suffix()"))
    cmds.setParent('..')

    cmds.showWindow(renamer_ui)


        
renamer()