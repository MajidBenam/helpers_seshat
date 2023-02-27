#!/bin/bash

echo "Before appending the files..."

# files_to_be_added (in this order):
file_1="1_base_imports.py"
file_2="2_all_views.py"
file_3="3_qing_vars_and_playground.py"

merged_file="all_files_merged.py"
source_abs_dir="/home/majid/dev/seshat/helpers/output_views/"
destination_abs_dir="/home/majid/dev/seshat/seshat/seshat/apps/crisisdb/"
destination_file="views.py"

rm $source_abs_dir$merged_file
cat  $source_abs_dir$file_1 $source_abs_dir$file_2 $source_abs_dir$file_3 > $source_abs_dir$merged_file
echo "Files appended successfully!"
cp $source_abs_dir$merged_file $destination_abs_dir$destination_file
echo "Contents of the merged file ($merged_file) successfully transferred to: $destination_abs_dir$destination_file!"
echo "SUCCESS!"