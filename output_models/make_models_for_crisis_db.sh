#!/bin/bash

echo "Before appending the files..."

# files_to_be_added (in this order):
file_1="1_models_imports_crisisdb.py"
file_2="2_choices_tuples.py"
file_3="3_models_function_definitions.py"
file_4="4_output_for_models.py"

merged_file="all_files_merged.py"
source_abs_dir="/home/majid/dev/seshat/helpers/output_models/"
destination_abs_dir="/home/majid/dev/seshat/seshat/seshat/apps/crisisdb/"
destination_file="models.py"

rm $source_abs_dir$merged_file
cat  $source_abs_dir$file_1 $source_abs_dir$file_2 $source_abs_dir$file_3 $source_abs_dir$file_4 > $source_abs_dir$merged_file
echo "Files appended successfully!"
cp $source_abs_dir$merged_file $destination_abs_dir$destination_file
echo "Contents of the merged file ($merged_file) successfully transferred to: $destination_abs_dir$destination_file!"
echo "SUCCESS!"