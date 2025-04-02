package com.azure.optimizer;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.charset.StandardCharsets;
import java.io.IOException;

public class FileReaderUtil {
    public static String readFileContent(String fileName) throws IOException {
        // Get absolute path dynamically
        String basePath = System.getProperty("user.dir") + "/demodata/";
        String filePath = basePath + fileName;

        return Files.readString(Paths.get(filePath), StandardCharsets.UTF_8);
    }
}
