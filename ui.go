import { UserInterface } from './user.interface';
import { User } from './user.model';
import { UserService } from './user.service';

export const UserProviders = [
  {
    provide: UserInterface,
    useClass: UserService,
  },
];

fn main() {
  const
  user = new User(),
  userService = new UserService();
  userService.create(user);
  console.log(user);
  userService.findAll();
  console.log(user);
}

  
