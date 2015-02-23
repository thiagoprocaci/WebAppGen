package #GROUP_NAME#.presentation;


import br.com.tbp.model.Customer;
import br.com.tbp.persistence.CustomerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import java.util.List;

@Controller
@RequestMapping("customer")
public class CustomerController {

    @Autowired
    private CustomerRepository customerRepository;


    @RequestMapping(value = "/findAll", method = RequestMethod.GET)
    public String findAll(Model model) {
        List<Customer> customerList = customerRepository.findAll();
        model.addAttribute("customerList", customerList);
        return "customer/customerList";

    }

}
