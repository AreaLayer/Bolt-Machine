import "fmt"
import "time"
import "conf"

func main() {

	fmt.Println("Hello World!")
	fmt.Println("Current time is", time.Now())
	fmt.Println("Config is", conf.Config)
}

func init() {
	conf.Config = "config.json"
}
