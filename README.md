# MegaToolsWrapper

(UNDER CONSTRUCTION)

Simple python Megatools wrapper

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cc71191c41f141bf99265cb2f096370b)](https://www.codacy.com/manual/Harkame/MegaToolsWrapper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Harkame/MegaToolsWrapper&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/b54097b0e1de916a9e19/maintainability)](https://codeclimate.com/github/Harkame/MegaToolsWrapper/maintainability)
[![Build Status](https://travis-ci.org/Harkame/MegaToolsWrapper.svg?branch=master)](https://travis-ci.org/Harkame/MegaToolsWrapper)
[![codecov](https://codecov.io/gh/Harkame/ScamNumberScraper/branch/master/graph/badge.svg)](https://codecov.io/gh/Harkame/ScamNumberScraper)

[Megatools](https://megatools.megous.com)

[Megatools (github)](https://github.com/megous/megatools)

## Installation

``` bash

pip install megatoolswrapper

```

## Usage

### Initialization

``` python

wrapper = MegaToolsWrapper()

#OR

wrapper = MegaToolsWrapper(megatools_path="D:\\megatools\\")

```

megatools_path : Directory where find all Megatools executable (megadl, megacopy, etc), if not specified, use Megatools command from path

### megacopy - synchronize local and remote mega.nz directories

``` python

wrapper.megacopy("https://mega.nz/#!PpVB0CTZ!bwa51HbeKaVjuCff_lzbH4nQnV27uBxmcF89PnnACvY")

```

### megadf - display mega.nz storage quotas/usage

``` python

wrapper.megadf("https://mega.nz/#!PpVB0CTZ!bwa51HbeKaVjuCff_lzbH4nQnV27uBxmcF89PnnACvY")

```

### megadl - download exported files from mega.nz

``` python

wrapper.megadl("https://mega.nz/#!PpVB0CTZ!bwa51HbeKaVjuCff_lzbH4nQnV27uBxmcF89PnnACvY")

```

### megaget - download individual files from mega.nz

``` python

wrapper.megaget("https://mega.nz/#!PpVB0CTZ!bwa51HbeKaVjuCff_lzbH4nQnV27uBxmcF89PnnACvY")

```

### megals - list files stored at mega.nz

``` python

wrapper.megals("https://mega.nz/#!PpVB0CTZ!bwa51HbeKaVjuCff_lzbH4nQnV27uBxmcF89PnnACvY")

```

### megamkdir - create directories at mega.nz

``` python

wrapper.megamkdir("https://mega.nz/#!PpVB0CTZ!bwa51HbeKaVjuCff_lzbH4nQnV27uBxmcF89PnnACvY")

```

### megaput - upload files to mega.nz

``` python

wrapper.megaput("https://mega.nz/#!PpVB0CTZ!bwa51HbeKaVjuCff_lzbH4nQnV27uBxmcF89PnnACvY")

```

### megareg - register a new mega.nz account

``` python

wrapper.megadl("https://mega.nz/#!PpVB0CTZ!bwa51HbeKaVjuCff_lzbH4nQnV27uBxmcF89PnnACvY")

```

### megarm - remove files from mega.nz

``` python

wrapper.megarm("https://mega.nz/#!PpVB0CTZ!bwa51HbeKaVjuCff_lzbH4nQnV27uBxmcF89PnnACvY")

```
