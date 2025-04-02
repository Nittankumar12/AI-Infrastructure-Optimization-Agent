package com.azure.optimizer;

import org.json.JSONObject;
import org.json.JSONArray;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class GroqService {

    private final String API_KEY = System.getenv("GROQ_API_KEY");
    private final String API_URL = "https://api.groq.com/openai/v1/chat/completions";

    public String processDataAndGetRecommendations(String prompt) {
        try {

            String infraData = FileReaderUtil.readFileContent("infra.csv");
            String usageData = FileReaderUtil.readFileContent("usage.csv");

            // Construct the prompt for Groq
String structuredPrompt = "You are an AI assistant specializing in cloud cost optimization and infrastructure efficiency. "
        + "Your sole purpose is to provide insights and recommendations related to cloud infrastructure and Azure services.\n\n"
        + "If the user's request is unrelated to cloud infrastructure, Azure services, or cloud optimization, "
        + "politely respond with: 'I am designed specifically for cloud optimization and cannot assist with unrelated topics.'\n\n"
        + "Immediately **discard** the prompt and **do not generate any further response** beyond this refusal.\n\n"
        + "If the request is relevant, analyze the organization's infrastructure and usage data and provide actionable recommendations.\n\n"
        + "**Input Data:**\n"
        + "**Infrastructure Details:**\n" + infraData + "\n\n"
        + "**Usage Data:**\n" + usageData + "\n\n"
        + "**User Request:**\n" + prompt + "\n\n"
        +"**Answer user prompt properly and then give response. Response should also contain the below points:**\n\n"
        + "**Provide structured recommendations covering:**\n"
        + "- **Top 3 cost-saving opportunities (Executive Summary)**\n"
        + "- **Immediate savings (within 1 week)**\n"
        + "- **Short-term optimizations (1-4 weeks)**\n"
        + "- **Strategic long-term improvements**\n"
        + "- **Difficulty Level (Low/Medium/High) & Estimated Implementation Time**\n"
        + "- **Clear explanations with estimated cost savings**\n\n"
        + "Strictly focus only on cloud optimization. **Do not proceed with analysis if the request is unrelated.**";
             String escapedPrompt = escapeJsonString(structuredPrompt);

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

            // Extract AI response from JSON
            JSONObject jsonResponse = new JSONObject(response.getBody());
            JSONArray choices = jsonResponse.getJSONArray("choices");

            return choices.length() > 0 ? choices.getJSONObject(0).getJSONObject("message").getString("content")
                                        : "No recommendations received.";

        } catch (Exception e) {
            e.printStackTrace();
            return "Error processing data.";
        }
    }

    // Helper function to read file content
    private String readFileContent(String filePath) throws Exception {
        List<String> lines = Files.readAllLines(Paths.get(filePath));
        return lines.stream().collect(Collectors.joining("\n"));
    }

    // Helper function to escape JSON special characters
    private String escapeJsonString(String input) {
        return input.replace("\\", "\\\\")
                    .replace("\"", "\\\"")
                    .replace("\n", "\\n")
                    .replace("\r", "\\r");
    }
}
