# SPDX-License-Identifier: Zlib
# kigo/compile/pipeline.py

import ast
from kigo.compile.ast_opt import KigoASTOptimizer


def kigo_compile(source: str, *, filename="<kigo>", release=False):
    tree = ast.parse(source, filename=filename)

    # AST optimization pass
    tree = KigoASTOptimizer(release=release).visit(tree)
    ast.fix_missing_locations(tree)

    # Compile with optimize flags
    optimize_level = 2 if release else 0
    return compile(tree, filename, "exec", optimize=optimize_level)