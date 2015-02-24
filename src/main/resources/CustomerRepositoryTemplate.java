package #GROUP_NAME#.persistence;


import java.util.List;

import #GROUP_NAME#.model.Customer;
import org.springframework.data.repository.CrudRepository;


public interface CustomerRepository extends CrudRepository<Customer, Long> {

    List<Customer> findByLastName(String lastName);

    List<Customer> findAll();
}