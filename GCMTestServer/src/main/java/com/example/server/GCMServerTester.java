package com.example.server;

import com.google.android.gcm.server.Message;
import com.google.android.gcm.server.Result;
import com.google.android.gcm.server.Sender;



public class GCMServerTester {
	  public static void main(String[] args) throws Exception {
		String apiKey = "AIzaSyAuSmpawGorpIBi6Y1GxtnW2ZZvIrkJi_8";
		String SENDER_ID = "381088048468";
	    sendMessage(apiKey);
	  }

	  private static void sendMessage(String apiKey) throws Exception {
	    String deviceId = "APA91bH4nWoYOYG1_tjssz_oIU1qTNI6uOhH9zXecqP70UdaDhXJE9pz8AnIPwj3DiuV3mZAAJIYjVPyiu5t29K7dB8T1ZvrGhb6PcfO9lucQurhNL-RFkugy_-A42S3fjLh22N6M3HFDX09552lPlOL4OhWuInPo7mBFNxsa0Wdlz8HazgvtW4";
	    Sender sender = new Sender(apiKey);
	    Message message = new Message.Builder().addData("data1", "New order from blah blah").build();
	    
	    Result result = sender.send(message, deviceId, 2);
	    System.out.println("result: " + result);
	  }
}
