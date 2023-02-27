#!/bin/bash

echo "Before appending the files..."

# files_to_be_added (in this order):
file_1="1_serializer_imports.py"
file_2="2_base_serializers.py"
file_3="3_output_for_all_crisisdb_serializers.py"

merged_file="all_files_merged.py"
source_abs_dir="/home/majid/dev/seshat/helpers/output_serializers/"
destination_abs_dir="/home/majid/dev/seshat/seshat/seshat/apps/seshat_api/"
destination_file="serializers.py"

rm $source_abs_dir$merged_file
cat  $source_abs_dir$file_1 $source_abs_dir$file_2 $source_abs_dir$file_3 > $source_abs_dir$merged_file
echo "Files appended successfully!"
cp $source_abs_dir$merged_file $destination_abs_dir$destination_file
echo "Contents of the merged file ($merged_file) successfully transferred to: $destination_abs_dir$destination_file!"
echo "SUCCESS!"
