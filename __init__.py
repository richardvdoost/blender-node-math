# Author: Rich Sedman
# Description: Dynamic Maths Expresion node Blender Add-on (Lite)
# Date: May 2018
################################################### History ######################################################
# 1.00 09/04/2019 : Initial version
# 1.01 24/04/2019 : Fixes to handling of operator precedence and negative terms
# 1.02 10/06/2019 : Include latest 'parse_expression.py' from 'full version' add-on
#                   Include bug fixes, documentation operator and all node types from 'full' version.
# 1.10 11/06/2019 : Minor bug fixes, include lite-specific documentation and 'upgrade' instructions.
# 1.11 21/07/2019 : Amend documentation to fix 'special variables' prefixes. Also, amend upgrade notes for blog url
#################################################################################################################

bl_info = {
    "name": "Node Math",
    "author": "Rich Sedman",
    "version": (1, 11),
    "blender": (3, 6, 0),
    "location": "Node Editor > Add",
    "description": (
        "Provide an option to create a new group from a typed maths expression (Lite)."
    ),
    "warning": (
        "This is the 'Lite' version - excludes the extended functionality of the full"
        " version."
    ),
    "wiki_url": "https://blendermarket.com/products/node-expressions",
    "tracker_url": "",
    "category": "Node",
}

import bpy
from nodeitems_utils import NodeItem
from nodeitems_utils import register_node_categories
from nodeitems_utils import unregister_node_categories

from .dynamic_maths_expression_node import DynamicMathsExpression_Operator
from .dynamic_maths_expression_node import DynamicMathsExpressionEdit_Operator
from .dynamic_maths_expression_node import DynamicMathsExpressionEditWithin_Operator
from .dynamic_maths_expression_node import DynamicMathsExpressionNode
from .dynamic_maths_expression_node import DynamicMathsExpressionRevert_Operator
from .dynamic_maths_expression_node import (
    DynamicMathsExpressionShowDocumentation_Operator,
)
from .dynamic_maths_expression_node import DynamicMathsExpressionShowUpgrade_Operator


def menu_draw(self, context):
    # Force 'invoke' when calling operator
    self.layout.operator_context = "INVOKE_DEFAULT"
    self.layout.operator("node.node_dynamic_maths_expression", text="Maths Expression")

    # Edit is not required since we can now edit within the group itself via the custom node
    # self.layout.operator("node.node_dynamic_maths_expression_edit", text='Maths Expression(Edit)')


bpy.types.NODE_MT_add.append(menu_draw)
# TODO : Need to add it to Add/Group rather than Add

classes = (
    DynamicMathsExpression_Operator,
    DynamicMathsExpressionEdit_Operator,
    DynamicMathsExpressionEditWithin_Operator,
    DynamicMathsExpressionRevert_Operator,
    DynamicMathsExpressionShowDocumentation_Operator,
    DynamicMathsExpressionShowUpgrade_Operator,
    DynamicMathsExpressionNode,
)


def register():
    from bpy.utils import register_class

    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class

    for cls in reversed(classes):
        unregister_class(cls)


if __name__ == "__main__":
    try:
        unregister()
    except:
        pass
    register()
