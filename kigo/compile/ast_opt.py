# SPDX-License-Identifier: Zlib
# kigo/compile/ast_opt.py

import ast


class KigoASTOptimizer(ast.NodeTransformer):
    def __init__(self, *, release: bool):
        self.release = release

    def visit_If(self, node):
        # Remove `if dev:` blocks in release
        if self.release and isinstance(node.test, ast.Name):
            if node.test.id == "dev":
                return None

        return self.generic_visit(node)

    def visit_Assert(self, node):
        # Strip asserts in release mode
        if self.release:
            return None
        return node