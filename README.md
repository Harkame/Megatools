# Megatools

(UNDER CONSTRUCTION)

Simple python Megatools wrapper

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/726d6cfd795242b587cdb8b8e9308f7c)](https://www.codacy.com/manual/Harkame/Megatools?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Harkame/Megatools&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/20a4bd84eaac4d6cdc9a/maintainability)](https://codeclimate.com/github/Harkame/Megatools/maintainability)
[Megatools](https://megatools.megous.com)

[Megatools (github)](https://github.com/megous/megatools)

## Installation

``` shell

pip install megatools

```

## Usage

### Initialization

``` python

from megatools import Megatools

megatools = Megatools() #Use megatools command in path

#OR

megatools = Megatools(executable="D:\\megatools\\megatools.exe")

```

### Get mega link filename

``` python

megatools.get_file_name("https://mega.nz/#!PpVB0CTZ!bwa51HbeKaVjuCff_lzbH4nQnV27uBxmcF89PnnACvY")

```

### dl - download exported files from mega.nz

``` python

megatools.dl("https://mega.nz/#!PpVB0CTZ!bwa51HbeKaVjuCff_lzbH4nQnV27uBxmcF89PnnACvY")

```

### Another commands incomming
