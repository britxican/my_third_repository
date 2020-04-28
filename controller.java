package com.taco.main;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.taco.servicesImpl.MongoService;
import com.taco.servicesImpl.ServiceImpl;
import com.taco.tacoEntity.TA;
import com.taco.tacoEntity.TacoAddTa;
import com.taco.tacoEntity.TacoAllTAs;
import com.taco.tacoEntity.TacoCourseTAAvailability;
import com.taco.tacoEntity.TacoCourseTAInformation;
import com.taco.tacoEntity.TacoCourseTask;
import com.taco.tacoEntity.TacoCourseTaskWithCourse;
import com.taco.tacoEntity.TacoDashboard;
import com.taco.tacoEntity.TacoProfCoursesAndRapidTeams;
import com.taco.tacoEntity.TacoUser;
import com.taco.tacoEntity.Url;
import com.taco.wfcEntities.person.Kronos_WFC;

@RestController
public class TacoController {

	@MessageMapping("/taco")
	@SendTo("/topic/tasks")
	public Response notifications(NotificationMessage message) throws Exception {
		Response response = new Response(message.getMessage(), message.getTime());
		return response;
	}

	@Autowired
	ServiceImpl serviceImpl;

	@Autowired
	TacoRepository tacoRepository;

	@Autowired
	MongoService mongoService;

	@RequestMapping(value = "www.lacucarachareloaded.com/data/loginUser.json", method = RequestMethod.GET)
	@ResponseBody
	public Url login(@RequestParam String userId) {
		String role = serviceImpl.getUserIdAndRole(userId);
		if (role.equals("Professor"))
			role = "prof";
		else
			role = "ta";
		return new Url("index.html#!/role/" + role + "/id/" + userId);
	}
