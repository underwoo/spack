##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class RDiagrammer(RPackage):
    """Create graph diagrams and flowcharts using R."""

    homepage = "https://github.com/rich-iannone/DiagrammeR"
    url      = "https://cran.r-project.org/src/contrib/DiagrammeR_0.8.4.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/DiagrammeR"

    version('0.8.4', '9ee295c744f5d4ba9a84289ca7bdaf1a')

    depends_on('r-htmlwidgets', type=('build', 'run'))
    depends_on('r-igraph', type=('build', 'run'))
    depends_on('r-influencer', type=('build', 'run'))
    depends_on('r-rstudioapi@0.6:', type=('build', 'run'))
    depends_on('r-stringr', type=('build', 'run'))
    depends_on('r-visnetwork', type=('build', 'run'))
    depends_on('r-scales', type=('build', 'run'))
