# DEMETER Data Preprocessing

Этот репозиторий содержит Python-скрипты для подготовки и преобразования данных космического аппарата **DEMETER** из бинарного формата `.dat` в пригодный для анализа `.csv`.

## Состав

- `merge_dat_files.py` — объединяет несколько `.dat` файлов в один.
- `demeter_dat_to_csv.py` — преобразует `.dat` файл в `.csv` формат для последующего анализа.

## Цель

Проект предназначен для подготовки экспериментальных данных спутника DEMETER к анализу, например, для визуализации, статистической обработки и машинного обучения.
В основе — данные с различных научных приборов, полученные в формате `.dat`.

Программа читает и обрабатывает файлы с различных APID, соответствующих следующим датчикам:
| APID | Датчик | Тип данных | Описание |
|------|-------------|------------|----------|
| 1129 | ICE         | ULFe WF    | Waveforms of 3 electric field components in ULF |
| 1130 | ICE         | ELFe WF    | Waveforms of 3 electric field components in ELF |
| 1131 | ICE         | VLFe WF    | Waveform of 1 electric field component in VLF   |
| 1132 | ICE         | VLFe SP    | Spectra of 1 electric field component in VLF    |
| 1133 | ICE         | HFe WF     | Waveform of 1 electric field component in HF    |
| 1134 | ICE         | HFe SP     | Spectra of 1 electric field component in HF     |
| 1135 | IMSC        | ELFb WF    | Waveforms of 3 magnetic field components in ELF |
| 1136 | IMSC        | VLFb WF    | Waveform of 1 magnetic field component in VLF   |
| 1137 | IMSC        | VLFb SP    | Spectra of 1 magnetic field component in  VLF   |
| 1138 | RNF         | NN result  | Detection results of the neural network         |
| 1139–1140 | IAP    | -          | Data of IAP experiment                          |
| 1141–1142 | IDP    | -          | Data of IDP experiment                          |
| 1143–1144 | ISL    | -          | Data of ISL experiment                          |

## Статус

Проект находится в разработке. На текущем этапе:
- Алгоритмы работают, но не оптимальны для обработки больших объемов данных.
- Гибкая структура данных (разное количество компонент, переменный формат) и разнообразие APID учитываются, но требуют улучшений по обработке.
- Планируется переработка `demeter_dat_to_csv.py` с учетом эффективного чтения блоков, филтрации полезных данных по координатам.

## Документация

Анализ и структура работы основаны на официальной документации миссии:
> **DEMETER Microsatellite – DATA PRODUCT DESCRIPTION**  
Prepared by: D. Lagoutte, J.Y. Brochot, D. de Carvalho, L. Madrias, M. Parrot  
Date: 17/06/2006  
Ref: **DMT-SP-9-CM-6054-LPC**, Edition . Revision 3.3  
Laboratoire de Physique et Chimie de l’Environnement  
Centre National de la Recherche Scientifique
