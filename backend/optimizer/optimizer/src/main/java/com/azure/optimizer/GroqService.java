package com.azure.optimizer;

import org.json.JSONObject;
import org.json.JSONArray;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.web.multipart.MultipartFile;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.stream.Collectors;

@Service
public class GroqService {

    private final String API_KEY = System.getenv("GROQ_API_KEY");
    private final String API_URL = "https://api.groq.com/openai/v1/chat/completions";

    public String processDataAndGetRecommendations(MultipartFile infraFile, MultipartFile usageFile, String prompt) {
        try {
            // Read uploaded CSV files into Strings
            String infraData = new BufferedReader(new InputStreamReader(infraFile.getInputStream()))
                    .lines().collect(Collectors.joining("\n"));
            String usageData = new BufferedReader(new InputStreamReader(usageFile.getInputStream()))
                    .lines().collect(Collectors.joining("\n"));

            // Construct the prompt
            String fullPrompt = "Infra:\n" + infraData + "\nUsage:\n" + usageData + "\nPrompt: " + prompt;
            String escapedPrompt = fullPrompt.replace("\n", "\\n").replace("\"", "\\\"");

            // Set up headers
            HttpHeaders headers = new HttpHeaders();
            headers.set("Authorization", "Bearer " + API_KEY);
            headers.set("Content-Type", "application/json");

            // Create JSON request body
            String requestBody = "{ \"model\": \"llama3-8b-8192\", \"messages\": [{\"role\": \"user\", \"content\": \"" + escapedPrompt + "\"}] }";

            // Send API request
            HttpEntity<String> requestEntity = new HttpEntity<>(requestBody, headers);
            RestTemplate restTemplate = new RestTemplate();
            ResponseEntity<String> response = restTemplate.postForEntity(API_URL, requestEntity, String.class);

            // Extract the AI's response from the JSON
            JSONObject jsonResponse = new JSONObject(response.getBody());
            JSONArray choices = jsonResponse.getJSONArray("choices");
            if (choices.length() > 0) {
                return choices.getJSONObject(0).getJSONObject("message").getString("content");
            }

            return "No recommendations received.";

        } catch (Exception e) {
            e.printStackTrace();
            return "Error processing data.";
        }
    }
}
