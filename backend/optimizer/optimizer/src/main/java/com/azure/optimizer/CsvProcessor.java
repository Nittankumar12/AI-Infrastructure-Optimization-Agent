package com.azure.optimizer;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;
import org.springframework.web.multipart.MultipartFile;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class CsvProcessor {

    public static List<Map<String, String>> parseCsv(MultipartFile file) throws IOException {
        List<Map<String, String>> dataList = new ArrayList<>();

        try (BufferedReader reader = new BufferedReader(new InputStreamReader(file.getInputStream()));
             CSVParser csvParser = new CSVParser(reader, CSVFormat.DEFAULT.withFirstRecordAsHeader())) {

            for (CSVRecord record : csvParser) {
                Map<String, String> data = new HashMap<>();
                for (String header : record.toMap().keySet()) {
                    data.put(header, record.get(header));
                }
                dataList.add(data);
            }
        }

        return dataList;
    }
}
